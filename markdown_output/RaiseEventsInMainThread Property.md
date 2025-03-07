Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseEventsInMainThread Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [NameSearchProcess Class](topic13195.md) : RaiseEventsInMainThread Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether or not events raised from this search process should be marshalled to the main thread. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property RaiseEventsInMainThread As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NameSearchProcess](topic13195.md)
    Dim value As Boolean
     
    instance.RaiseEventsInMainThread = value
     
    value = instance.RaiseEventsInMainThread  
  
C#|   
---|---  
      
    
    public bool RaiseEventsInMainThread {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NameSearchProcess Class](topic13195.md)   
[NameSearchProcess Members](topic13196.md)


