Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterBooleanProperty(String,FlowPropertyInfo,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperties Class](topic10905.md) > [RegisterBooleanProperty Method](topic10915.md) : RegisterBooleanProperty(String,FlowPropertyInfo,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the property.

_info_
    Information about the property.

_defaultValue_
    The default value for the property.

Glossary Item Box

Creates a new specification flow property which can store boolean data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RegisterBooleanProperty( _
       ByVal _name_ As String, _
       ByVal _info_ As [FlowPropertyInfo](topic10992.md), _
       ByVal _defaultValue_ As Boolean _
    ) As [FlowProperty(Of Boolean)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperties](topic10905.md)
    Dim name As String
    Dim info As [FlowPropertyInfo](topic10992.md)
    Dim defaultValue As Boolean
    Dim value As [FlowProperty(Of Boolean)](topic10978.md)
     
    value = instance.RegisterBooleanProperty(name, info, defaultValue)  
  
C#|   
---|---  
      
    
    public [FlowProperty<bool>](topic10978.md) RegisterBooleanProperty( 
       string _name_ ,
       [FlowPropertyInfo](topic10992.md) _info_ ,
       bool _defaultValue_
    )  
  
#### Parameters

 _name_
    The name of the property.
_info_
    Information about the property.
_defaultValue_
    The default value for the property.

#### Return Value

A new specification flow property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperties Class](topic10905.md)   
[FlowProperties Members](topic10906.md)   
[Overload List](topic10915.md)


