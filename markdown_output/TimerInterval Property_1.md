       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TimerInterval Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6835.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Folder Namespace](topic6821.md) > [FolderWatcherConfiguration Class](topic6823.md) : TimerInterval Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the time in seconds for the period of time to wait between scans of the source folder. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property TimerInterval As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FolderWatcherConfiguration](topic6823.md)
    Dim value As Integer
     
    instance.TimerInterval = value
     
    value = instance.TimerInterval  
  
C#|   
---|---  
      
    
    public int TimerInterval {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FolderWatcherConfiguration Class](topic6823.md)   
[FolderWatcherConfiguration Members](topic6824.md)

©2024 DriveWorks Ltd. All Rights Reserved.
