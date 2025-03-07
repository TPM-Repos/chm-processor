Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FailedInputNames Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [SpecificationRequestInputsDrivenEventArgs Class](topic1960.md) : FailedInputNames Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the names of the inputs that were unable to be driven. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property FailedInputNames As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationRequestInputsDrivenEventArgs](topic1960.md)
    Dim value() As String
     
    value = instance.FailedInputNames  
  
C#|   
---|---  
      
    
    public string[] FailedInputNames {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationRequestInputsDrivenEventArgs Class](topic1960.md)   
[SpecificationRequestInputsDrivenEventArgs Members](topic1961.md)


