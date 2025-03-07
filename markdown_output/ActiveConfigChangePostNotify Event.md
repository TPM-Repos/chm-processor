Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActiveConfigChangePostNotify Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : ActiveConfigChangePostNotify Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the configuration of the current Assembly changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ActiveConfigChangePostNotify As EventHandler(Of ResultEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim handler As EventHandler(Of ResultEventArgs)
     
    AddHandler instance.ActiveConfigChangePostNotify, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ResultEventArgs> ActiveConfigChangePostNotify  
  
# Event Data

The event handler receives an argument of type [ResultEventArgs](topic13909.md) containing data related to this event. The following **ResultEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Success](topic13916.md)| Gets/sets the result of the event (default is True).   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


