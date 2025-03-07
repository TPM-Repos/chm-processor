Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileOpenPostNotify Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : FileOpenPostNotify Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised by SolidWorks after a file has been opened. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event FileOpenPostNotify As EventHandler(Of FileOpenNotifyEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim handler As EventHandler(Of FileOpenNotifyEventArgs)
     
    AddHandler instance.FileOpenPostNotify, handler  
  
C#|   
---|---  
      
    
    event EventHandler<FileOpenNotifyEventArgs> FileOpenPostNotify  
  
# Event Data

The event handler receives an argument of type [FileOpenNotifyEventArgs](topic13653.md) containing data related to this event. The following **FileOpenNotifyEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Filename](topic13660.md)| Gets the name of the file that was opened.   
[Success](topic13916.md)| Gets/sets the result of the event (default is True). (Inherited from [DriveWorks.SolidWorks.ResultEventArgs](topic13909.md))  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


