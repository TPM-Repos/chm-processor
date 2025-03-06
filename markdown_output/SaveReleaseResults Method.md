       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SaveReleaseResults Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3266.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : SaveReleaseResults Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_results_
    The results to save to the database.

Glossary Item Box

Saves the results of releasing one or more components. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SaveReleaseResults( _
       ByVal _results_ As [ReleaseComponentsResults](topic6300.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim results As [ReleaseComponentsResults](topic6300.md)
     
    instance.SaveReleaseResults(results)  
  
C#|   
---|---  
      
    
    public void SaveReleaseResults( 
       [ReleaseComponentsResults](topic6300.md) _results_
    )  
  
#### Parameters

 _results_
    The results to save to the database.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)

©2024 DriveWorks Ltd. All Rights Reserved.
