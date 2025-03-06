SearchedItem Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleSearchProcess Class](topic13212.md) : SearchedItem Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs for every item that is searched by the search process. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SearchedItem As EventHandler(Of RuleSearchResultEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleSearchProcess](topic13212.md)
    Dim handler As EventHandler(Of RuleSearchResultEventArgs)
     
    AddHandler instance.SearchedItem, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RuleSearchResultEventArgs> SearchedItem  
  
# Event Data

The event handler receives an argument of type [RuleSearchResultEventArgs](topic13242.md) containing data related to this event. The following **RuleSearchResultEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Item](topic13248.md)| The found item from the search.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleSearchProcess Class](topic13212.md)   
[RuleSearchProcess Members](topic13213.md)


