![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SerializationMode Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7318.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : SerializationMode Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Controls the serialization of a control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum SerializationMode 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SerializationMode](topic7318.md)  
  
C#|   
---|---  
      
    
    public enum SerializationMode : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**Backup**|  Serializes the information required to backup the control.  
**Copy**|  Serializes the information required to duplicate the control.  
**Display**|  Serializes the information required to display the control to and end-user.  
**Save**|  Serializes the information required to save the control to a file as part of the project, and reload it when the project is loaded.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Forms.SerializationMode**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Forms Namespace](topic7266.md)

©2024 DriveWorks Ltd. All Rights Reserved.
