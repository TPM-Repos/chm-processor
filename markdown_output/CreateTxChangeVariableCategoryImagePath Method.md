![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeVariableCategoryImagePath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13019.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeVariableCategoryImagePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variableCategory_
    The variable category to change.

_newImagePath_
    The new image path.

Glossary Item Box

Creates a transaction which, when committed, will change the specified variable category's image path. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeVariableCategoryImagePath( _
       ByVal _variableCategory_ As [ProjectVariableCategory](topic4983.md), _
       ByVal _newImagePath_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variableCategory As [ProjectVariableCategory](topic4983.md)
    Dim newImagePath As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeVariableCategoryImagePath(variableCategory, newImagePath)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeVariableCategoryImagePath( 
       [ProjectVariableCategory](topic4983.md) _variableCategory_ ,
       string _newImagePath_
    )  
  
#### Parameters

 _variableCategory_
    The variable category to change.
_newImagePath_
    The new image path.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
