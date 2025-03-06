![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterStatic(Type,String,String,String,String,String,Object,Type) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9436.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) > [RegisterStatic Method](topic9435.md) : RegisterStatic(Type,String,String,String,String,String,Object,Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlType_
    The type of the control.

_storeName_
    The name of a custom backing data store.

_serializeAs_
    The name of the property used to serialize/deserialize the property.

_displayName_
    The name of the property as it should be shown in UI.

_description_
    The description of the property which should be shown in UI.

_category_
    The category of the property when shown in UI.

_defaultValue_
    The default value of the property.

_clrType_
    The CLR type of the value stored by the property.

Glossary Item Box

Registers a static property, which has the same backing store name as serialization name, for the given type of control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function RegisterStatic( _
       ByVal _controlType_ As Type, _
       ByVal _storeName_ As String, _
       ByVal _serializeAs_ As String, _
       ByVal _displayName_ As String, _
       ByVal _description_ As String, _
       ByVal _category_ As String, _
       ByVal _defaultValue_ As Object, _
       ByVal _clrType_ As Type _
    ) As [DynamicProperty](topic9398.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controlType As Type
    Dim storeName As String
    Dim serializeAs As String
    Dim displayName As String
    Dim description As String
    Dim category As String
    Dim defaultValue As Object
    Dim clrType As Type
    Dim value As [DynamicProperty](topic9398.md)
     
    value = [DynamicProperty](topic9398.md).RegisterStatic(controlType, storeName, serializeAs, displayName, description, category, defaultValue, clrType)  
  
C#|   
---|---  
      
    
    public static [DynamicProperty](topic9398.md) RegisterStatic( 
       Type _controlType_ ,
       string _storeName_ ,
       string _serializeAs_ ,
       string _displayName_ ,
       string _description_ ,
       string _category_ ,
       object _defaultValue_ ,
       Type _clrType_
    )  
  
#### Parameters

 _controlType_
    The type of the control.
_storeName_
    The name of a custom backing data store.
_serializeAs_
    The name of the property used to serialize/deserialize the property.
_displayName_
    The name of the property as it should be shown in UI.
_description_
    The description of the property which should be shown in UI.
_category_
    The category of the property when shown in UI.
_defaultValue_
    The default value of the property.
_clrType_
    The CLR type of the value stored by the property.

#### Return Value

A dynamic property for the control.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)   
[Overload List](topic9435.md)

©2024 DriveWorks Ltd. All Rights Reserved.
