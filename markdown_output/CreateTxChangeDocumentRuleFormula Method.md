![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeDocumentRuleFormula Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12966.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeDocumentRuleFormula Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_document_
    The document in which the rule exists.

_rule_
    The name of the rule whose formula to change.

_newFormula_
    The new formula to apply.

Glossary Item Box

Creates a transaction which, when committed, will change the rule of the specified ProjectDocumentRule 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeDocumentRuleFormula( _
       ByVal _document_ As [ProjectDocument](topic4356.md), _
       ByVal _rule_ As [ProjectDocumentRule](topic4399.md), _
       ByVal _newFormula_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim document As [ProjectDocument](topic4356.md)
    Dim rule As [ProjectDocumentRule](topic4399.md)
    Dim newFormula As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeDocumentRuleFormula(document, rule, newFormula)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeDocumentRuleFormula( 
       [ProjectDocument](topic4356.md) _document_ ,
       [ProjectDocumentRule](topic4399.md) _rule_ ,
       string _newFormula_
    )  
  
#### Parameters

 _document_
    The document in which the rule exists.
_rule_
    The name of the rule whose formula to change.
_newFormula_
    The new formula to apply.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
