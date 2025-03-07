Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProcessEnded Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [IEventReportWriter Interface](topic10336.md) : ProcessEnded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a process is ended. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ProcessEnded As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IEventReportWriter](topic10336.md)
    Dim handler As EventHandler
     
    AddHandler instance.ProcessEnded, handler  
  
C#|   
---|---  
      
    
    event EventHandler ProcessEnded  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IEventReportWriter Interface](topic10336.md)   
[IEventReportWriter Members](topic10337.md)


