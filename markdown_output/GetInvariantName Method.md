Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetInvariantName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) : GetInvariantName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_assembly_
    The assembly for which to get the extension library name.

Glossary Item Box

Gets the invariant name from an extension library. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetInvariantName( _
       ByVal _assembly_ As Assembly _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [LibraryAttribute](topic7201.md)
    Dim assembly As Assembly
    Dim value As String
     
    value = instance.GetInvariantName(assembly)  
  
C#|   
---|---  
      
    
    public string GetInvariantName( 
       Assembly _assembly_
    )  
  
#### Parameters

 _assembly_
    The assembly for which to get the extension library name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)


