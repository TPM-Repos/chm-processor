Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTypesFromLibraries Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryManager Interface](topic2079.md) : GetTypesFromLibraries Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_baseType_
    The type of a class from which the returned types must inherit, or an interface which the returned types must implement.

_attributes_
    An array of attributes which must be defined on the returned types, or a null reference if no attribute filtering is required.

Glossary Item Box

Gets types which inherit from the specified base type, or implement the specified interface. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetTypesFromLibraries( _
       ByVal _baseType_ As Type, _
       ByVal _attributes_() As Type _
    ) As Type()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryManager](topic2079.md)
    Dim baseType As Type
    Dim attributes() As Type
    Dim value() As Type
     
    value = instance.GetTypesFromLibraries(baseType, attributes)  
  
C#|   
---|---  
      
    
    Type[] GetTypesFromLibraries( 
       Type _baseType_ ,
       Type[] _attributes_
    )  
  
#### Parameters

 _baseType_
    The type of a class from which the returned types must inherit, or an interface which the returned types must implement.
_attributes_
    An array of attributes which must be defined on the returned types, or a null reference if no attribute filtering is required.

#### Return Value

An array of types meeting the specified filter.

# Remarks

The base type must implement the [DriveWorks.Extensibility.IExtension](topic7152.md) interface to be discoverable using this method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryManager Interface](topic2079.md)   
[ILibraryManager Members](topic2080.md)


