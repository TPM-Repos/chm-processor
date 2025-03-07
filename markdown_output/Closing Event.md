Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Closing Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.RulesBuilder Namespace](topic1581.md) > [IRulesBuilder Interface](topic1590.md) : Closing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised by the RulesBuilder when it is closing. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Closing As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IRulesBuilder](topic1590.md)
    Dim handler As EventHandler
     
    AddHandler instance.Closing, handler  
  
C#|   
---|---  
      
    
    event EventHandler Closing  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IRulesBuilder Interface](topic1590.md)   
[IRulesBuilder Members](topic1591.md)


