Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FlowPropertyInfo Constructor(String,String,String[],Boolean)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowPropertyInfo Class](topic10992.md) > [FlowPropertyInfo Constructor](topic10998.md) : FlowPropertyInfo Constructor(String,String,String[],Boolean)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_description_
    The description of the property.

_category_
    The category to which the property belongs.

_propertyTypes_
    The semantic types that apply to the property.

_isRequired_
    True if this property has to be given a value before the task it is associated with can execute.

Glossary Item Box

Initializes a new instance of the [FlowPropertyInfo](topic10992.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _description_ As String, _
       ByVal _category_ As String, _
       ByVal _propertyTypes_() As String, _
       ByVal _isRequired_ As Boolean _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim description As String
    Dim category As String
    Dim propertyTypes() As String
    Dim isRequired As Boolean
     
    Dim instance As New [FlowPropertyInfo](topic10992.md)(description, category, propertyTypes, isRequired)  
  
C#|   
---|---  
      
    
    public FlowPropertyInfo( 
       string _description_ ,
       string _category_ ,
       string[] _propertyTypes_ ,
       bool _isRequired_
    )  
  
#### Parameters

 _description_
    The description of the property.
_category_
    The category to which the property belongs.
_propertyTypes_
    The semantic types that apply to the property.
_isRequired_
    True if this property has to be given a value before the task it is associated with can execute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowPropertyInfo Class](topic10992.md)   
[FlowPropertyInfo Members](topic10993.md)   
[Overload List](topic10998.md)


