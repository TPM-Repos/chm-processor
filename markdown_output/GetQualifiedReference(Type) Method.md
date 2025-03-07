Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetQualifiedReference(Type) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) > [GetQualifiedReference Method](topic7218.md) : GetQualifiedReference(Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    A type defined in an extension library.

Glossary Item Box

Gets a qualified reference for the specified type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function GetQualifiedReference( _
       ByVal _type_ As Type _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim type As Type
    Dim value As String
     
    value = [LibraryAttribute](topic7201.md).GetQualifiedReference(type)  
  
C#|   
---|---  
      
    
    public static string GetQualifiedReference( 
       Type _type_
    )  
  
#### Parameters

 _type_
    A type defined in an extension library.

#### Return Value

A qualified reference for the type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)   
[Overload List](topic7218.md)


