Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsFrameworkLibrary Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [FrameworkLibraryAttribute Class](topic7183.md) : IsFrameworkLibrary Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_assembly_
    The assembly to test.

Glossary Item Box

Tests the specified assembly to see whether it is a framework library. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function IsFrameworkLibrary( _
       ByVal _assembly_ As Assembly _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim assembly As Assembly
    Dim value As Boolean
     
    value = [FrameworkLibraryAttribute](topic7183.md).IsFrameworkLibrary(assembly)  
  
C#|   
---|---  
      
    
    public static bool IsFrameworkLibrary( 
       Assembly _assembly_
    )  
  
#### Parameters

 _assembly_
    The assembly to test.

#### Return Value

True if the specified assembly is marked with the [FrameworkLibraryAttribute](topic7183.md) and is signed with the DriveWorks strong name key.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FrameworkLibraryAttribute Class](topic7183.md)   
[FrameworkLibraryAttribute Members](topic7184.md)


