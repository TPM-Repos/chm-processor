       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UsageFound Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [NameSearchProcess Class](topic13195.md) : UsageFound Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an instance of use has been found. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event UsageFound As EventHandler(Of SearchEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NameSearchProcess](topic13195.md)
    Dim handler As EventHandler(Of SearchEventArgs)
     
    AddHandler instance.UsageFound, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SearchEventArgs> UsageFound  
  
# Event Data

The event handler receives an argument of type [SearchEventArgs](topic13263.md) containing data related to this event. The following **SearchEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Item](topic13269.md)| The found item from the search.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NameSearchProcess Class](topic13195.md)   
[NameSearchProcess Members](topic13196.md)


