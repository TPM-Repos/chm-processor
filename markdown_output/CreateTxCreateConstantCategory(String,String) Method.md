![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateConstantCategory(String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13044.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateConstantCategory Method](topic13042.md) : CreateTxCreateConstantCategory(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the new category.

_parentCategoryPath_
    Optionally, the parent category path, or a null reference to leave the category rooted.

Glossary Item Box

Creates a transaction which, when committed, will create a new constant category. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateConstantCategory( _
       ByVal _displayName_ As String, _
       ByVal _parentCategoryPath_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim displayName As String
    Dim parentCategoryPath As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateConstantCategory(displayName, parentCategoryPath)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateConstantCategory( 
       string _displayName_ ,
       string _parentCategoryPath_
    )  
  
#### Parameters

 _displayName_
    The display name of the new category.
_parentCategoryPath_
    Optionally, the parent category path, or a null reference to leave the category rooted.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13042.md)

©2024 DriveWorks Ltd. All Rights Reserved.
