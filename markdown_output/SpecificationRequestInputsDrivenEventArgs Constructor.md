       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationRequestInputsDrivenEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [SpecificationRequestInputsDrivenEventArgs Class](topic1960.md) : SpecificationRequestInputsDrivenEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_failedInputNames_
    The names of the inputs that were unable to be driven.

Glossary Item Box

Initializes a new instance of the [SpecificationRequestInputsDrivenEventArgs](topic1960.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _failedInputNames_() As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim failedInputNames() As String
     
    Dim instance As New [SpecificationRequestInputsDrivenEventArgs](topic1960.md)(failedInputNames)  
  
C#|   
---|---  
      
    
    public SpecificationRequestInputsDrivenEventArgs( 
       string[] _failedInputNames_
    )  
  
#### Parameters

 _failedInputNames_
    The names of the inputs that were unable to be driven.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationRequestInputsDrivenEventArgs Class](topic1960.md)   
[SpecificationRequestInputsDrivenEventArgs Members](topic1961.md)


