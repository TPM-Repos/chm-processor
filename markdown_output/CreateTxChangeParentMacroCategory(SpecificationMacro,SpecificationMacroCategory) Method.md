![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeParentMacroCategory(SpecificationMacro,SpecificationMacroCategory) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12988.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeParentMacroCategory Method](topic12987.md) : CreateTxChangeParentMacroCategory(SpecificationMacro,SpecificationMacroCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    The specification macro to modify.

_newCategory_
    The new parent category, or a null reference to remove the parent.

Glossary Item Box

Creates a transaction which when committed will change the parent category of the specified specification macro. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeParentMacroCategory( _
       ByVal _macro_ As [SpecificationMacro](topic11429.md), _
       ByVal _newCategory_ As [SpecificationMacroCategory](topic5359.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim newCategory As [SpecificationMacroCategory](topic5359.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeParentMacroCategory(macro, newCategory)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeParentMacroCategory( 
       [SpecificationMacro](topic11429.md) _macro_ ,
       [SpecificationMacroCategory](topic5359.md) _newCategory_
    )  
  
#### Parameters

 _macro_
    The specification macro to modify.
_newCategory_
    The new parent category, or a null reference to remove the parent.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic12987.md)

©2024 DriveWorks Ltd. All Rights Reserved.
