TryParseQualifiedReference Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) : TryParseQualifiedReference Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reference_
    The reference to parse.

_namespaceName_
    The namespace of the referenced type, or an empty string if no namespace is present.

_typeName_
    The unqualified name of the referenced type.

_libraryName_
    The name of the library containing the referenced type.

Glossary Item Box

Attempts to parse a qualified reference. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function TryParseQualifiedReference( _
       ByVal _reference_ As String, _
       ByRef _namespaceName_ As String, _
       ByRef _typeName_ As String, _
       ByRef _libraryName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim reference As String
    Dim namespaceName As String
    Dim typeName As String
    Dim libraryName As String
    Dim value As Boolean
     
    value = [LibraryAttribute](topic7201.md).TryParseQualifiedReference(reference, namespaceName, typeName, libraryName)  
  
C#|   
---|---  
      
    
    public static bool TryParseQualifiedReference( 
       string _reference_ ,
       out string _namespaceName_ ,
       out string _typeName_ ,
       out string _libraryName_
    )  
  
#### Parameters

 _reference_
    The reference to parse.
_namespaceName_
    The namespace of the referenced type, or an empty string if no namespace is present.
_typeName_
    The unqualified name of the referenced type.
_libraryName_
    The name of the library containing the referenced type.

#### Return Value

True if the parse was successful, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)


