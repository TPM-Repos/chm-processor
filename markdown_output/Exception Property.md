Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Exception Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [TransitionFailedEventArgs Class](topic1968.md) : Exception Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The exception that occurred during execution of the transition, e.g. if the transition could not be found, or the user doesn't have permissions to access the transition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Exception As Exception  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TransitionFailedEventArgs](topic1968.md)
    Dim value As Exception
     
    value = instance.Exception  
  
C#|   
---|---  
      
    
    public Exception Exception {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TransitionFailedEventArgs Class](topic1968.md)   
[TransitionFailedEventArgs Members](topic1969.md)


