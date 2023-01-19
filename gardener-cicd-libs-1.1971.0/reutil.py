import re
import typing

T = typing.TypeVar


def re_filter(
    include_regexes: typing.Iterable[str] = (),
    exclude_regexes: typing.Iterable[str] = (),
    value_transformation: typing.Callable[[T], str] = None,
    re_flags: int=0,
) -> typing.Callable[[typing.Union[T, str]], bool]:
    '''
    returns a callable that can be used as a filter, applying the given include and exclude
    regular expressions. The matching semantics is defined so that the absence of filter values
    disables filtering.

    Regexes must fully match. It is sufficient if any include or exclude regex matches. Exclusion
    has precedence.

    @param include_regexes: iterable[str]: value matches if any regex matches (fullmatch)
    @param exclude_regexes: iterable[str]: value is excluded if any regex matches (fullmatch)
    @param value_transformation: callable: optional transformation for value; should yield str
    '''
    include_functions = [re.compile(r, re_flags).fullmatch for r in include_regexes]
    exclude_functions = [re.compile(r, re_flags).fullmatch for r in exclude_regexes]

    def _re_filter(value):
        if value_transformation:
            value = value_transformation(value)

        matches = True
        if include_functions:
            matches &= any(
                map(lambda f: f(value), include_functions)
            )

        # exclusion filter has precedence
        if exclude_functions:
            matches &= not any(
                map(lambda f: f(value), exclude_functions)
            )

        return matches

    return _re_filter
