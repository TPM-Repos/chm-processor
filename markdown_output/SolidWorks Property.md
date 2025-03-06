       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SolidWorks Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13416.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksService Interface](topic13411.md) : SolidWorks Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the current instance of SolidWorks, or a null reference (Nothing in Visual Basic) if the application is not connected to SolidWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property SolidWorks As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksService](topic13411.md)
    Dim value As Object
     
    value = instance.SolidWorks  
  
C#|   
---|---  
      
    
    object SolidWorks {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksService Interface](topic13411.md)   
[ISolidWorksService Members](topic13412.md)

©2024 DriveWorks Ltd. All Rights Reserved.
