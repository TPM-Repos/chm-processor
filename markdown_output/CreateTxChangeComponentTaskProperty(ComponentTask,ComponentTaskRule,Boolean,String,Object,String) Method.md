Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeComponentTaskProperty(ComponentTask,ComponentTaskRule,Boolean,String,Object,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeComponentTaskProperty Method](topic12946.md) : CreateTxChangeComponentTaskProperty(ComponentTask,ComponentTaskRule,Boolean,String,Object,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task whose rule will be changed.

_rule_
    The rule to change.

_ruleBound_
    

_formula_
    The new formula to give the rule.

_value_
    

_comment_
    The new comment to give the rule.

Glossary Item Box

Creates a new transaction that when executed will change the formula and comment of the given [DriveWorks.Components.Tasks.ComponentTask](topic6407.md) rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeComponentTaskProperty( _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _rule_ As [ComponentTaskRule](topic6704.md), _
       ByVal _ruleBound_ As Boolean, _
       ByVal _formula_ As String, _
       ByVal _value_ As Object, _
       ByVal _comment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim rule As [ComponentTaskRule](topic6704.md)
    Dim ruleBound As Boolean
    Dim formula As String
    Dim value As Object
    Dim comment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeComponentTaskProperty(task, rule, ruleBound, formula, value, comment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeComponentTaskProperty( 
       [ComponentTask](topic6407.md) _task_ ,
       [ComponentTaskRule](topic6704.md) _rule_ ,
       bool _ruleBound_ ,
       string _formula_ ,
       object _value_ ,
       string _comment_
    )  
  
#### Parameters

 _task_
    The task whose rule will be changed.
_rule_
    The rule to change.
_ruleBound_
    
_formula_
    The new formula to give the rule.
_value_
    
_comment_
    The new comment to give the rule.

#### Return Value

A transaction that when executed will change the formula and comment of the given rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic12946.md)


