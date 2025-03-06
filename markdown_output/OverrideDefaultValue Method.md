![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OverrideDefaultValue Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9427.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : OverrideDefaultValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlType_
    The type of the control for which to override the default value.

_dynamicProperty_
    The dynamic property to override.

_defaultValue_
    The new default value for the specified control type.

Glossary Item Box

Overrides the default value of the property for the given type, which derives from the type which defines the property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub OverrideDefaultValue( _
       ByVal _controlType_ As Type, _
       ByVal _dynamicProperty_ As [DynamicProperty](topic9398.md), _
       ByVal _defaultValue_ As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controlType As Type
    Dim dynamicProperty As [DynamicProperty](topic9398.md)
    Dim defaultValue As Object
     
    [DynamicProperty](topic9398.md).OverrideDefaultValue(controlType, dynamicProperty, defaultValue)  
  
C#|   
---|---  
      
    
    public static void OverrideDefaultValue( 
       Type _controlType_ ,
       [DynamicProperty](topic9398.md) _dynamicProperty_ ,
       object _defaultValue_
    )  
  
#### Parameters

 _controlType_
    The type of the control for which to override the default value.
_dynamicProperty_
    The dynamic property to override.
_defaultValue_
    The new default value for the specified control type.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)

©2024 DriveWorks Ltd. All Rights Reserved.
