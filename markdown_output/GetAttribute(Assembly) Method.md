Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAttribute(Assembly) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) > [GetAttribute Method](topic7214.md) : GetAttribute(Assembly) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_assembly_
    The assembly from which to retrieve the attribute.

Glossary Item Box

Gets the [LibraryAttribute](topic7201.md) from the specified assembly. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function GetAttribute( _
       ByVal _assembly_ As Assembly _
    ) As [LibraryAttribute](topic7201.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim assembly As Assembly
    Dim value As [LibraryAttribute](topic7201.md)
     
    value = [LibraryAttribute](topic7201.md).GetAttribute(assembly)  
  
C#|   
---|---  
      
    
    public static [LibraryAttribute](topic7201.md) GetAttribute( 
       Assembly _assembly_
    )  
  
#### Parameters

 _assembly_
    The assembly from which to retrieve the attribute.

#### Return Value

An instance of the library attribute if it is applied to the specified assembly, otherwise a null reference (Nothing in Visual Basic).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)   
[Overload List](topic7214.md)


