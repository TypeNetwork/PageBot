#!/bin/bash
export WONT_FIX=invalid-name,bad-indentation,trailing-newlines,wrong-import-position,fixme
export CATCHALL_MAY_FIX_LATER=line-too-long,trailing-whitespace,duplicate-code,bad-whitespace,no-name-in-module,import-error,multiple-imports,bad-continuation,no-value-for-parameter,too-many-arguments,too-many-locals,unused-argument,pointless-string-statement,using-constant-test,invalid-encoded-data,too-many-instance-attributes,too-few-public-methods,attribute-defined-outside-init,protected-access,wrong-import-order,missing-final-newline,mixed-indentation,unused-variable,no-member,too-many-function-args,unexpected-keyword-arg,bare-except,no-self-use,no-method-argument,function-redefined,too-many-public-methods,anomalous-backslash-in-string,redefined-builtin,too-many-branches,relative-import,arguments-differ,syntax-error,reimported,used-before-assignment,too-many-boolean-expressions,too-many-statements,no-self-argument,unnecessary-pass,keyword-arg-before-vararg,not-a-mapping,multiple-statements,inconsistent-return-statements,pointless-statement,ungrouped-imports,unnecessary-semicolon,no-else-return,old-style-class,too-many-nested-blocks,unsubscriptable-object,too-many-lines,unidiomatic-typecheck,bare-except,simplifiable-if-statement,too-many-return-statements,blacklisted-name,exec-used,not-callable,eval-used,empty-docstring,super-init-not-called,singleton-comparison,unreachable,expression-not-assigned,consider-using-enumerate,unbalanced-tuple-unpacking,global-statement,duplicate-key,anomalous-unicode-escape-in-string,no-init,redefined-argument-from-local,broad-except,missing-docstring,superfluous-parens,wildcard-import,unused-wildcard-import,redefined-outer-name,consider-iterating-dictionary
export PYLINT="pylint --disable=$WONT_FIX,$CATCHALL_MAY_FIX_LATER"
$PYLINT Lib/pagebot
