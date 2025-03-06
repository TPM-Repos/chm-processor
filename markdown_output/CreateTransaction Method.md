![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTransaction Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13233.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleSearchResult Class](topic13227.md) : CreateTransaction Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    

_factory_
    The [DriveWorks.Transactions.ProjectTransactionFactory](topic12928.md) used to create the transaction.

_rule_
    The new rule to apply.

Glossary Item Box

Creates a new transaction responsible for changing the rule of the item. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function CreateTransaction( _
       ByVal _project_ As [Project](topic3859.md), _
       ByVal _factory_ As [ProjectTransactionFactory](topic12928.md), _
       ByVal _rule_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleSearchResult](topic13227.md)
    Dim project As [Project](topic3859.md)
    Dim factory As [ProjectTransactionFactory](topic12928.md)
    Dim rule As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTransaction(project, factory, rule)  
  
C#|   
---|---  
      
    
    public abstract [ITransaction](topic12837.md) CreateTransaction( 
       [Project](topic3859.md) _project_ ,
       [ProjectTransactionFactory](topic12928.md) _factory_ ,
       string _rule_
    )  
  
#### Parameters

 _project_
    
_factory_
    The [DriveWorks.Transactions.ProjectTransactionFactory](topic12928.md) used to create the transaction.
_rule_
    The new rule to apply.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleSearchResult Class](topic13227.md)   
[RuleSearchResult Members](topic13228.md)

©2024 DriveWorks Ltd. All Rights Reserved.
