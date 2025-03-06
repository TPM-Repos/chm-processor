![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeProjectComponentRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12993.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeProjectComponentRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rule_
    The rule to update.

_formula_
    The new formula to set on the rule.

_comment_
    The new comment to set on the rule.

Glossary Item Box

Creates a transaction that will change the rule of the specified component rule. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeProjectComponentRule( _
       ByVal _rule_ As [ProjectComponentRule](topic6198.md), _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim rule As [ProjectComponentRule](topic6198.md)
    Dim formula As String
    Dim comment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeProjectComponentRule(rule, formula, comment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeProjectComponentRule( 
       [ProjectComponentRule](topic6198.md) _rule_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _rule_
    The rule to update.
_formula_
    The new formula to set on the rule.
_comment_
    The new comment to set on the rule.

#### Return Value

A transaction that will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
