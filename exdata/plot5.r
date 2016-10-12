library('ggplot2')
library('cowplot')

Baltimore<-NEI[NEI$fips=='24510',]
s_vehicle<-SCC[grep('Vehicle',SCC$Short.Name),]
ve<-Baltimore[Baltimore$SCC %in% s_vehicle$SCC,]
em<-aggregate(Emissions~year,data=ve,FUN=sum)

g1<-ggplot(data=ve,aes(x=as.factor(year)))+geom_boxplot(aes(y=log(Emissions)))+xlab('Year')+ggtitle('Boxplot of Emissions from Motor Vehicle in Baltimore City')

g2<-ggplot(data=em,aes(x=as.factor(year),y=Emissions))+geom_point()+geom_line(aes(group=1))+xlab('Year')+ylab('Emissions (T)')+ggtitle('Total Emissions from Motor Vehicle in Baltimore City')

plot_grid(g1,g2,ncol=1)

ggsave('plot5.png',width=5.5,height = 4)
