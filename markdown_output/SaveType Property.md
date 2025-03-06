       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SaveType Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13669.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileSavePostNotifyEventArgs Class](topic13661.md) : SaveType Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the type of save as defined in swFileSaveTypes_e. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property SaveType As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileSavePostNotifyEventArgs](topic13661.md)
    Dim value As Integer
     
    value = instance.SaveType  
  
C#|   
---|---  
      
    
    public int SaveType {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileSavePostNotifyEventArgs Class](topic13661.md)   
[FileSavePostNotifyEventArgs Members](topic13662.md)

©2024 DriveWorks Ltd. All Rights Reserved.
