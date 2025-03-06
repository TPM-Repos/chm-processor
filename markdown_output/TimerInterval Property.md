       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TimerInterval Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6784.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) > [DatabaseConnectorConfiguration Class](topic6756.md) : TimerInterval Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the time between checks to the database for new data to process. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property TimerInterval As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DatabaseConnectorConfiguration](topic6756.md)
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

[DatabaseConnectorConfiguration Class](topic6756.md)   
[DatabaseConnectorConfiguration Members](topic6757.md)

©2024 DriveWorks Ltd. All Rights Reserved.
