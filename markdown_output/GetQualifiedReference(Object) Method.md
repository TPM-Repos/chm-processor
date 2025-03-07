Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetQualifiedReference(Object) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) > [GetQualifiedReference Method](topic7218.md) : GetQualifiedReference(Object) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_instance_
    An object whose type is defined in an extension library.

Glossary Item Box

Gets a qualified reference for the specified object's type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function GetQualifiedReference( _
       ByVal _instance_ As Object _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As Object
    Dim value As String
     
    value = [LibraryAttribute](topic7201.md).GetQualifiedReference(instance)  
  
C#|   
---|---  
      
    
    public static string GetQualifiedReference( 
       object _instance_
    )  
  
#### Parameters

 _instance_
    An object whose type is defined in an extension library.

#### Return Value

A qualified reference for the object's type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)   
[Overload List](topic7218.md)


