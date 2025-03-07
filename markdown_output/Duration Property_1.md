Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Duration Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectProfileEvent Class](topic4681.md) : Duration Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The length of time this event took to complete (or current run time if it hasn't completed yet). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides ReadOnly Property Duration As TimeSpan  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectProfileEvent](topic4681.md)
    Dim value As TimeSpan
     
    value = instance.Duration  
  
C#|   
---|---  
      
    
    public override TimeSpan Duration {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectProfileEvent Class](topic4681.md)   
[ProjectProfileEvent Members](topic4682.md)


