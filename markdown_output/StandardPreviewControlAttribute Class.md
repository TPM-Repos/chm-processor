       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StandardPreviewControlAttribute Class   
[Members](topic1060.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1059.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : StandardPreviewControlAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about a control that should be used to preview supported files. 

# Object Model

![](dotnetdiagramimages/image36.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=True, 
       Inherited=True)>
    Public Class StandardPreviewControlAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StandardPreviewControlAttribute](topic1059.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=true, 
       Inherited=true)]
    public class StandardPreviewControlAttribute : System.Attribute   
  
# Remarks

A class which implements the [IPreviewControl](topic362.md) interface must be marked with one of the following attributes.

  * [StandardPreviewControlAttribute](topic1059.md)
  * [DynamicPreviewControlAttribute](topic784.md)
  * [ConfigurablePreviewControlAttribute](topic729.md)



# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Applications.StandardPreviewControlAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StandardPreviewControlAttribute Members](topic1060.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
