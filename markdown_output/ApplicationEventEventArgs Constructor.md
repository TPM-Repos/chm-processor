Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationEventEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ApplicationEventEventArgs Class](topic663.md) : ApplicationEventEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_evt_
    The event.

Glossary Item Box

Initializes a new instance of the [ApplicationEventEventArgs](topic663.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _evt_ As [IApplicationEvent](topic36.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim evt As [IApplicationEvent](topic36.md)
     
    Dim instance As New [ApplicationEventEventArgs](topic663.md)(evt)  
  
C#|   
---|---  
      
    
    public ApplicationEventEventArgs( 
       [IApplicationEvent](topic36.md) _evt_
    )  
  
#### Parameters

 _evt_
    The event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ApplicationEventEventArgs Class](topic663.md)   
[ApplicationEventEventArgs Members](topic664.md)


