![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Register(Type,String,Object,PropertyBehavior,Type,DynamicPropertyData) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9432.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) > [Register Method](topic9428.md) : Register(Type,String,Object,PropertyBehavior,Type,DynamicPropertyData) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlType_
    The type of the control.

_storeName_
    The name of a custom backing data store.

_defaultValue_
    The default value of the property.

_behavior_
    The behavior of the property, i.e. whether it is static or dynamic.

_clrType_
    The CLR type of the value stored by the property.

_data_
    Additional settings for the property.

Glossary Item Box

Registers a dynamic property, which has the same backing store name as serialization name, for the given type of control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Register( _
       ByVal _controlType_ As Type, _
       ByVal _storeName_ As String, _
       ByVal _defaultValue_ As Object, _
       ByVal _behavior_ As [PropertyBehavior](topic9383.md), _
       ByVal _clrType_ As Type, _
       ByVal _data_ As [DynamicPropertyData](topic9456.md) _
    ) As [DynamicProperty](topic9398.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controlType As Type
    Dim storeName As String
    Dim defaultValue As Object
    Dim behavior As [PropertyBehavior](topic9383.md)
    Dim clrType As Type
    Dim data As [DynamicPropertyData](topic9456.md)
    Dim value As [DynamicProperty](topic9398.md)
     
    value = [DynamicProperty](topic9398.md).Register(controlType, storeName, defaultValue, behavior, clrType, data)  
  
C#|   
---|---  
      
    
    public static [DynamicProperty](topic9398.md) Register( 
       Type _controlType_ ,
       string _storeName_ ,
       object _defaultValue_ ,
       [PropertyBehavior](topic9383.md) _behavior_ ,
       Type _clrType_ ,
       [DynamicPropertyData](topic9456.md) _data_
    )  
  
#### Parameters

 _controlType_
    The type of the control.
_storeName_
    The name of a custom backing data store.
_defaultValue_
    The default value of the property.
_behavior_
    The behavior of the property, i.e. whether it is static or dynamic.
_clrType_
    The CLR type of the value stored by the property.
_data_
    Additional settings for the property.

#### Return Value

A dynamic property for the control.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)   
[Overload List](topic9428.md)

©2024 DriveWorks Ltd. All Rights Reserved.
