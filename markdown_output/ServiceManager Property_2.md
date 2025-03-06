       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ServiceManager Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic32.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplication Interface](topic24.md) : ServiceManager Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the object responsible for managing services for the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property ServiceManager As [IServiceManager](topic435.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplication](topic24.md)
    Dim value As [IServiceManager](topic435.md)
     
    value = instance.ServiceManager  
  
C#|   
---|---  
      
    
    [IServiceManager](topic435.md) ServiceManager {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplication Interface](topic24.md)   
[IApplication Members](topic25.md)

©2024 DriveWorks Ltd. All Rights Reserved.
