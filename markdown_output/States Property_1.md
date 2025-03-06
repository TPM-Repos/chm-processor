       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
States Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13882.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ProhibitedStatesAttribute Class](topic13875.md) : States Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the list of application states where this entity should not be visible. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property States As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProhibitedStatesAttribute](topic13875.md)
    Dim value() As String
     
    value = instance.States  
  
C#|   
---|---  
      
    
    public string[] States {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProhibitedStatesAttribute Class](topic13875.md)   
[ProhibitedStatesAttribute Members](topic13876.md)

©2024 DriveWorks Ltd. All Rights Reserved.
