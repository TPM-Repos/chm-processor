![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateVariableCategory(String,ProjectVariableCategory) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13078.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateVariableCategory Method](topic13077.md) : CreateTxCreateVariableCategory(String,ProjectVariableCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the new category.

_parentCategory_
    Optionally, the parent category, or a null reference to leave the category rooted.

Glossary Item Box

Creates a transaction which, when committed, will create a new variable category. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateVariableCategory( _
       ByVal _displayName_ As String, _
       ByVal _parentCategory_ As [ProjectVariableCategory](topic4983.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim displayName As String
    Dim parentCategory As [ProjectVariableCategory](topic4983.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateVariableCategory(displayName, parentCategory)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateVariableCategory( 
       string _displayName_ ,
       [ProjectVariableCategory](topic4983.md) _parentCategory_
    )  
  
#### Parameters

 _displayName_
    The display name of the new category.
_parentCategory_
    Optionally, the parent category, or a null reference to leave the category rooted.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13077.md)

©2024 DriveWorks Ltd. All Rights Reserved.
