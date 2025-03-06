![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateConstant(String,ProjectConstantCategory) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstants Class](topic4246.md) > [CreateConstant Method](topic4252.md) : CreateConstant(String,ProjectConstantCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name to assign to the constant.

_category_
    The parent category, or a null reference (Nothing in Visual Basic) to leave the constant without a parent category.

Glossary Item Box

Creates a new constant with the specified name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads MustOverride Function CreateConstant( _
       ByVal _displayName_ As String, _
       ByVal _category_ As [ProjectConstantCategory](topic4219.md) _
    ) As [ProjectConstant](topic4171.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstants](topic4246.md)
    Dim displayName As String
    Dim category As [ProjectConstantCategory](topic4219.md)
    Dim value As [ProjectConstant](topic4171.md)
     
    value = instance.CreateConstant(displayName, category)  
  
C#|   
---|---  
      
    
    public abstract [ProjectConstant](topic4171.md) CreateConstant( 
       string _displayName_ ,
       [ProjectConstantCategory](topic4219.md) _category_
    )  
  
#### Parameters

 _displayName_
    The display name to assign to the constant.
_category_
    The parent category, or a null reference (Nothing in Visual Basic) to leave the constant without a parent category.

#### Return Value

The newly created constant.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectConstants Class](topic4246.md)   
[ProjectConstants Members](topic4247.md)   
[Overload List](topic4252.md)


