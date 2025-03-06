![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeComponentTaskRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeComponentTaskRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task whose rule will be changed.

_rule_
    The rule to change.

_formula_
    The new formula to give the rule.

_comment_
    The new comment to give the rule.

Glossary Item Box

Creates a new transaction that when executed will change the formula and comment of the given [DriveWorks.Components.Tasks.ComponentTask](topic6407.md) rule. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeComponentTaskRule( _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _rule_ As [ComponentTaskRule](topic6704.md), _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim rule As [ComponentTaskRule](topic6704.md)
    Dim formula As String
    Dim comment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeComponentTaskRule(task, rule, formula, comment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeComponentTaskRule( 
       [ComponentTask](topic6407.md) _task_ ,
       [ComponentTaskRule](topic6704.md) _rule_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _task_
    The task whose rule will be changed.
_rule_
    The rule to change.
_formula_
    The new formula to give the rule.
_comment_
    The new comment to give the rule.

#### Return Value

A transaction that when executed will change the formula and comment of the given rule.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


