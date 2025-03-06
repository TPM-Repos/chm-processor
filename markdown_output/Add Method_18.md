![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedDimensionCollection Class](topic14838.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The DriveWorks name of the dimension.

_address_
    The SolidWorks address of the dimension.

_value_
    The value of the dimension.

Glossary Item Box

Adds a new dimension to the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _address_ As String, _
       ByVal _value_ As String _
    ) As [ReleasedDimension](topic14826.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedDimensionCollection](topic14838.md)
    Dim name As String
    Dim address As String
    Dim value As String
    Dim value As [ReleasedDimension](topic14826.md)
     
    value = instance.Add(name, address, value)  
  
C#|   
---|---  
      
    
    public [ReleasedDimension](topic14826.md) Add( 
       string _name_ ,
       string _address_ ,
       string _value_
    )  
  
#### Parameters

 _name_
    The DriveWorks name of the dimension.
_address_
    The SolidWorks address of the dimension.
_value_
    The value of the dimension.

#### Return Value

The newly created dimension.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedDimensionCollection Class](topic14838.md)   
[ReleasedDimensionCollection Members](topic14839.md)


