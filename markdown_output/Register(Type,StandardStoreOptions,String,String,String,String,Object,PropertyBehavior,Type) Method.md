Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Register(Type,StandardStoreOptions,String,String,String,String,Object,PropertyBehavior,Type) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) > [Register Method](topic9428.md) : Register(Type,StandardStoreOptions,String,String,String,String,Object,PropertyBehavior,Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlType_
    The type of the control.

_standardStore_
    One of a number of predefined property backing stores.

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

_behavior_
    The behavior of the property, i.e. whether it is static or dynamic.

_clrType_
    The CLR type of the value stored by the property.

Glossary Item Box

Registers a dynamic property for the given type of control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Register( _
       ByVal _controlType_ As Type, _
       ByVal _standardStore_ As [StandardStoreOptions](topic9384.md), _
       ByVal _serializeAs_ As String, _
       ByVal _displayName_ As String, _
       ByVal _description_ As String, _
       ByVal _category_ As String, _
       ByVal _defaultValue_ As Object, _
       ByVal _behavior_ As [PropertyBehavior](topic9383.md), _
       ByVal _clrType_ As Type _
    ) As [DynamicProperty](topic9398.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim controlType As Type
    Dim standardStore As [StandardStoreOptions](topic9384.md)
    Dim serializeAs As String
    Dim displayName As String
    Dim description As String
    Dim category As String
    Dim defaultValue As Object
    Dim behavior As [PropertyBehavior](topic9383.md)
    Dim clrType As Type
    Dim value As [DynamicProperty](topic9398.md)
     
    value = [DynamicProperty](topic9398.md).Register(controlType, standardStore, serializeAs, displayName, description, category, defaultValue, behavior, clrType)  
  
C#|   
---|---  
      
    
    public static [DynamicProperty](topic9398.md) Register( 
       Type _controlType_ ,
       [StandardStoreOptions](topic9384.md) _standardStore_ ,
       string _serializeAs_ ,
       string _displayName_ ,
       string _description_ ,
       string _category_ ,
       object _defaultValue_ ,
       [PropertyBehavior](topic9383.md) _behavior_ ,
       Type _clrType_
    )  
  
#### Parameters

 _controlType_
    The type of the control.
_standardStore_
    One of a number of predefined property backing stores.
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
_behavior_
    The behavior of the property, i.e. whether it is static or dynamic.
_clrType_
    The CLR type of the value stored by the property.

#### Return Value

A dynamic property for the control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)   
[Overload List](topic9428.md)


