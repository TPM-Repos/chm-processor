![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedCustomPropertyCollection Class](topic14812.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the custom property.

_value_
    The value of the custom property.

Glossary Item Box

Adds and returns a new custom property with the given name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _value_ As String _
    ) As [ReleasedCustomProperty](topic14804.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedCustomPropertyCollection](topic14812.md)
    Dim name As String
    Dim value As String
    Dim value As [ReleasedCustomProperty](topic14804.md)
     
    value = instance.Add(name, value)  
  
C#|   
---|---  
      
    
    public [ReleasedCustomProperty](topic14804.md) Add( 
       string _name_ ,
       string _value_
    )  
  
#### Parameters

 _name_
    The name of the custom property.
_value_
    The value of the custom property.

#### Return Value

The newly added custom property.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedCustomPropertyCollection Class](topic14812.md)   
[ReleasedCustomPropertyCollection Members](topic14813.md)


