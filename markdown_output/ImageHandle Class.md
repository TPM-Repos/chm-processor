Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ImageHandle Class   
[Members](topic855.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : ImageHandle Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The common base class for image handles such as [StandardImageHandle](topic1051.md) and [ManagedImageHandle](topic867.md). 

# Object Model

![](dotnetdiagramimages/image20.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public MustInherit Class ImageHandle   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ImageHandle](topic854.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public abstract class ImageHandle   
  
# Remarks

DriveWorks uses images in a number of places for UI extensibility, image handles allow plugins to use either built-in image resources (via the [StandardImageHandle](topic1051.md) class) or provide their own (via the [ManagedImageHandle](topic867.md) class).

# Inheritance Hierarchy

System.Object  
**DriveWorks.Applications.ImageHandle**  
[DriveWorks.Applications.ManagedImageHandle](topic867.md)  
[DriveWorks.Applications.StandardImageHandle](topic1051.md)  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ImageHandle Members](topic855.md)   
[DriveWorks.Applications Namespace](topic16.md)


