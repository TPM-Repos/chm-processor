UsageFound Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleSearchProcess Class](topic13212.md) : UsageFound Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a match has been found. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event UsageFound As EventHandler(Of RuleSearchResultEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleSearchProcess](topic13212.md)
    Dim handler As EventHandler(Of RuleSearchResultEventArgs)
     
    AddHandler instance.UsageFound, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RuleSearchResultEventArgs> UsageFound  
  
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


