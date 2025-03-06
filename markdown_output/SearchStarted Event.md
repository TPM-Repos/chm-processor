       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SearchStarted Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10304.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : SearchStarted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the search phase of the rename process has started. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SearchStarted As EventHandler(Of SearchStartedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler(Of SearchStartedEventArgs)
     
    AddHandler instance.SearchStarted, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SearchStartedEventArgs> SearchStarted  
  
# Event Data

The event handler receives an argument of type [SearchStartedEventArgs](topic10326.md) containing data related to this event. The following **SearchStartedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Names](topic10333.md)| Gets the names that are being searched for.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)

©2024 DriveWorks Ltd. All Rights Reserved.
