Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AreReferencesEqual Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) : AreReferencesEqual Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reference1_
    The first reference to compare.

_reference2_
    The second reference to compare.

Glossary Item Box

Compares two qualified references for equality. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function AreReferencesEqual( _
       ByVal _reference1_ As String, _
       ByVal _reference2_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim reference1 As String
    Dim reference2 As String
    Dim value As Boolean
     
    value = [LibraryAttribute](topic7201.md).AreReferencesEqual(reference1, reference2)  
  
C#|   
---|---  
      
    
    public static bool AreReferencesEqual( 
       string _reference1_ ,
       string _reference2_
    )  
  
#### Parameters

 _reference1_
    The first reference to compare.
_reference2_
    The second reference to compare.

#### Return Value

True if the references are equivalent, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)


