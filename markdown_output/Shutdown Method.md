       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Shutdown Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2315.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IShutdownable Interface](topic2310.md) : Shutdown Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Shuts down the object. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Shutdown()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IShutdownable](topic2310.md)
     
    instance.Shutdown()  
  
C#|   
---|---  
      
    
    void Shutdown()  
  
# Remarks

This function should act as a way to dispose of an object when processing has finished, rather than performing an immediate disposal.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IShutdownable Interface](topic2310.md)   
[IShutdownable Members](topic2311.md)

©2024 DriveWorks Ltd. All Rights Reserved.
